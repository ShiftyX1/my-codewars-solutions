export function greet(name: string, owner: string): string{
  return owner === name ? "Hello boss" : "Hello guest";
}