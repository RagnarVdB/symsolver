function getCorrespondingBracket(input, firstIndex) {
  if (input[firstIndex] === '(') {
    let open = 0
    let close = 0
    for (let i = firstIndex + 1; i < input.length; i++) {
      if (input[i] == '('){
        open++
      }
      if (input[i] == ')') {
        if (open == close) {
          return i
        }
        close++
      }
    }
  } else if (input[firstIndex] === ')') {
    let open = 0
    let close = 0
    for (let i=firstIndex - 1; i >= 0;  i--) {
      if (input[i] == '('){
        if (open == close) {
          return i
        }
        open++
      }
      if (input[i] == ')') {
        close++
      }
    }
  }
  else {
    throw 'Not a bracket'
  }
}

function latexGenerator(input) {
  // spaties en machten
  let string = input.replace(/\*\*/g, '^').replace(/ /g, '')

  // keywords
  const keywords = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'arcsin', 'arccos', 'arctan', 'log', 'ln', 'sqrt', 'sinh', 'cosh', 'tanh']
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
        string = string.slice(0, index) + '(' + string.slice(index, end) + ')' + string.slice(end, string.length)
        extraChars += 2
      } else {
        return 'invalid'
      }
      
    }
  }
  // deling
  const max_loop = 20
  let j = 0
  while (string.indexOf('/') !== -1 && j < max_loop) {
    j++
    const i = string.indexOf('/')
    let leftBlockStart
    if (string[i-1] === ')') {
      let found = false
      let pos =  getCorrespondingBracket(string, i-1)
      let k = 0
      while (!found && k < max_loop) {
        k++
        if (string[pos-1] === '^') {
          if (string[pos-2] === ')') {
            pos = getCorrespondingBracket(string, pos-2)
          } else {
            found = true
            leftBlockStart = pos - 2
          }
        }
        else {
          found = true
          leftBlockStart = pos
        }
      }
    } else {
      leftBlockStart = i-1
    }
    string = string.slice(0, leftBlockStart) + ' \\frac {' + string.slice(leftBlockStart, string.length).replace('/', '} ')
  }
  // doe onnodige haakjes weg
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '^' && string[i+1] === '(') {
      const closing = getCorrespondingBracket(string, i+1)
      if (string[closing + 1] !== '^') {
        string = string.slice(0, i + 1) + '{' + string.slice(i + 2, string.length)
        string = string.slice(0, closing) + '}' + string.slice(closing + 1, string.length)
      }
    }
  }
  if (string[0] === '(' && getCorrespondingBracket(string, 0) === string.length - 1) {
    string = string.slice(1, string.length - 1)
  }
  return string.replace(/\(/g, '{(' ).replace(/\)/g, ')}').replace(/\*/g, ' \\cdot ')
}

 export default latexGenerator
// console.log(latexGenerator('sin(x) + e^sin(x)'))
