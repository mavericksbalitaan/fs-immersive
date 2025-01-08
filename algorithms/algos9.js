function pushVal(array, num) {
  // let newarr = [];
  // newarr.push(num)
  // for (let i = 0; i < array.length; i++) {
  //   newarr.push(array[i])
  // }
  // return newarr

  // or
  let newarr = [];
  for (let i = 0; i < array.length; i++) {
    newarr[i+1] = array[i]
  }
  newarr[0] = num;

  return newarr;
}

console.log(pushVal([2, 3, 4, 5], 1))
