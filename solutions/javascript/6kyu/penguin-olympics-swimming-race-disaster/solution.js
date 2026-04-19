function calculateWinners(snapshot, penguins) {
  let place = snapshot.replace(/~/g, '--').match(/p-*/gi).map((d, i) => [ d.length, penguins[i] ]).sort((a, b) => a[0] - b[0]).map(p => p[1]);
  return `GOLD: ${place[0]}, SILVER: ${place[1]}, BRONZE: ${place[2]}`;
}