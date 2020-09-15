const forward = {
  '(': ')',
  '{': '}',
  '[':']'
}
const backward = {
  ')': '(',
  '}': '{',
  ']':'['
}

const keywords = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'arcsin', 'arccos', 'arctan', 'log', 'ln', 'sinh', 'cosh', 'tanh']

function getCorrespondingBracket(input, firstIndex) {
  // Geeft voor open haakje in formule het corresponderend sluithaakje of omgekeerd
  if (input[firstIndex] in forward) {
    const openbracket = input[firstIndex]
    const closebracket = forward[input[firstIndex]]
    let open = 0
    let close = 0
    for (let i = firstIndex + 1; i < input.length; i++) {
      if (input[i] === openbracket){
        open++
      }
      if (input[i] === closebracket) {
        if (open == close) {
          return i
        }
        close++
      }
    }
  } else if (input[firstIndex] in backward) {
    const openbracket = backward[input[firstIndex]]
    const closebracket = input[firstIndex]
    let open = 0
    let close = 0
    for (let i=firstIndex - 1; i >= 0;  i--) {
      if (input[i] === openbracket){
        if (open == close) {
          return i
        }
        open++
      }
      if (input[i] === closebracket) {
        close++
      }
    }
  }
  else {
    throw 'Not a bracket'
  }
}

function bracketKeywords(string) {
  // Plaatst {} rond keywords zodat ze niet uit elkaar worden getrokken
  for (const keyword of keywords) {
    const regex = new RegExp(keyword, 'g')
    const indices = []
    let result
    while ( (result = regex.exec(string)) ) {
      indices.push(result.index)
    }
    let extraChars = 0
    for (const previndex of indices) {
      const index = previndex + extraChars
      const end = getCorrespondingBracket(string, index + keyword.length)
      if (string[index + keyword.length] === '(' && end) {
        string = string.slice(0, index) + '{' + string.slice(index, end + 1) + '}' + string.slice(end + 1, string.length)
        extraChars += 2
      } else {
        throw 'invalid keyword'
      }
      
    }
  }
  return string
}

function bracketPowers(string) {
  let i = 0
  while (i < string.length) {
    if (string[i] === '^') {
      const left = (string[i - 1] in backward) ? getCorrespondingBracket(string, i - 1) : i - 1
      const right = (string[i + 1] in forward) ? getCorrespondingBracket(string, i + 1) : i + 1
      string = string.slice(0, left) + '{' + string.slice(left, right + 1) + '}' + string.slice(right + 1, string.length)
      i++
    }
    i++
  }
  return string
}

function division(string) {
  const stop = ['(', ')', '{','}', '+', '-', '*', '/']
  const max_loop = 20
  let j = 0
  while (string.indexOf('/') !== -1 && j < max_loop) {
    j++
    const i = string.indexOf('/')
    let leftBlockStart
    let leftbracket = false
    let rightblockend
    if (string[i-1] in backward) {
      leftBlockStart = getCorrespondingBracket(string, i-1)
    } else {
      // vind eerste spatie of operator
      leftbracket = true 
      let k = i - 1
      let found = false
      while (!found && k >= 0) {
        if (stop.includes(string[i])) {
          found = true
        }
        k--
      }
      leftBlockStart = k + 1
    }
    if (string[i+1] in forward) {
      rightblockend = false
    } else {
      let k = i + 1
      let found = false
      while (!found && k <= string.length) {
        if (stop.includes(string[i])) {
          found = true
        }
        k++
      }
      rightblockend = k - 1
    }
    if (rightblockend && leftbracket) {
      string = string.slice(0, leftBlockStart) + ' \\frac {' + string.slice(leftBlockStart, i) + '} {' + string.slice(i + 1, rightblockend + 1) + '}' + string.slice(rightblockend + 1, string.length)
    } else if (leftbracket){
      string = string.slice(0, leftBlockStart) + ' \\frac {' + string.slice(leftBlockStart, string.length).replace('/', '} ')
    } else if (rightblockend) {
      string = string.slice(0, leftBlockStart) + ' \\frac ' + string.slice(leftBlockStart, i) + ' {' + string.slice(i + 1, rightblockend + 1) + '}' + string.slice(rightblockend + 1, string.length)
    } else {
      string = string.slice(0, leftBlockStart) + ' \\frac ' + string.slice(leftBlockStart, i) + string.slice(i + 1, string.length)
    }
  }
  if (j === max_loop) throw 'couldn\'t solve formula'
  return string
}

function sqrtHandler(string) {
  const reg = /sqrt\(/g
  let result
  const indices = []
  while ( (result = reg.exec(string)) ) {
    indices.push(result.index)
  }
  let extraChars = 0
  for (const i of indices) {
    const firstIndex = i + extraChars
    const lastIndex = getCorrespondingBracket(string, firstIndex + 4)
    string = string.slice(0, firstIndex) + '{\\sqrt{' + string.slice(firstIndex + 5, lastIndex) + '}}' + string.slice(lastIndex + 1, string.length)
    extraChars += 2
  }
  return string
}

function latexGenerator(input) {
  if ((input.match(/\(/g) || []).length !== (input.match(/\)/g) || []).length) {
    throw 'invalid number of brackets'
  }
  // spaties en machten
  let string = input.replace(/\*\*/g, '^').replace(/ /g, '')
  // vierkantswortels
  string = sqrtHandler(string)
  // Getallen samenhouden
  string = string.replace(/\d+/g, '{$&}')

  // Keywords samenhouden
  string = bracketKeywords(string)

  // Machten samenhouden
  string = bracketPowers(string)
  // deling
  string = division(string)
  // // doe onnodige haakjes weg
  // for (let i = 0; i < string.length; i++) {
  //   if (string[i] === '^' && string[i+1] === '(') {
  //     const closing = getCorrespondingBracket(string, i+1)
  //     if (string[closing + 1] !== '^') {
  //       string = string.slice(0, i + 1) + '{' + string.slice(i + 2, string.length)
  //       string = string.slice(0, closing) + '}' + string.slice(closing + 1, string.length)
  //     }
  //   }
  // }
  // if (string[0] === '(' && getCorrespondingBracket(string, 0) === string.length - 1) {
  //   string = string.slice(1, string.length - 1)
  // }
  return string.replace(/\(/g, '{(' ).replace(/\)/g, ')}').replace(/\*/g, ' \\cdot ')
}

export default latexGenerator
