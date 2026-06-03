let a = 10,
  b = 20,
  c = 30,
  d = 40;
let max;

if (a >= b) {
  if (a >= c) {
    if (a >= d) {
      max = a;
    } else {
      max = d;
    }
  } else {
    if (c >= d) {
      max = c;
    } else {
      max = d;
    }
  }
} else {
  if (b >= c) {
    if (b >= d) {
      max = b;
    } else {
      max = d;
    }
  } else {
    if (c >= d) {
      max = c;
    } else {
      max = d;
    }
  }
}

console.log("The maximum number is: " + max);
