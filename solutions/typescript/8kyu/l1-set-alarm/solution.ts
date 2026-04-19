export function setAlarm(employed: boolean, vacation: boolean) {
  if (vacation || !employed) {
    return false
  }
  return true
}