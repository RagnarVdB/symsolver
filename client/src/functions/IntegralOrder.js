function checkCorrectOrder(variables, usedVars) {
  // checkt of de variabelen in de juiste volgorde staan om geïntegreerd te worden
  const allowed = []
  for (const variable of variables) {
    for (const usedVar of usedVars[variable]) {
      if (!allowed.includes(usedVar)) {
        return false
      }
    }
    allowed.push(variable)
  }
  return true
}

function perm(xs) {
  // geeft permutaties van array
  let ret = [];
  for (let i = 0; i < xs.length; i++) {
    let rest = perm(xs.slice(0, i).concat(xs.slice(i + 1)));
    if(rest.length === 0) {
      ret.push([xs[i]])
    } else {
      for(let j = 0; j < rest.length; j++) {
        ret.push([xs[i]].concat(rest[j]))
      }
    }
  }
  return ret;
}

function getCorrectOrder(bounds, usedVars) {
  // geeft juiste volgorde integralen
  const permuts = perm(bounds)
  console.log(permuts)
  for (const perm of permuts) {
    if (checkCorrectOrder(perm.map(el => el[0]), usedVars)) {
      return perm
    }
  }
  return false
}

export default getCorrectOrder
