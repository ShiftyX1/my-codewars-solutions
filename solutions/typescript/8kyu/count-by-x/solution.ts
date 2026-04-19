export function countBy(x: number, n: number): number[] {
  return [...Array(n).keys()].map(i=> (i+1)*x);
}