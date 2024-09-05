items = [
  { name: "#1", weight: 1, profit: 4 },
  { name: "#2", weight: 3, profit: 9 },
  { name: "#3", weight: 5, profit: 12 },
  { name: "#4", weight: 4, profit: 11 },
];

max_weight = 8;

dp = [];

// adding empty item to make the code more readable
items.splice(0, 0, { name: "#0", weight: 0, profit: 0 });

for (var i = 0; i < items.length; i++) {
  // In JS sometimes if we using 2D array, we need to assign the array to an empty one to start using it
  dp[i] = [];
  for (var j = 0; j <= max_weight; j++) {
    if (i == 0 || j == 0) {
      dp[i][j] = 0;
    } else if (items[i].weight <= j) {
      dp[i][j] = Math.max(
        items[i].profit + dp[i - 1][j - items[i].weight],
        dp[i - 1][j]
      );
    } else {
      // top cell
      dp[i][j] = dp[i - 1][j];
    }
  }
}

// console.log(dp);
console.log("Max Profit:", dp[items.length - 1][max_weight]);

solution = [];
i = items.length - 1;
j = max_weight;
remain = max_weight;

while (remain >= 0 && j > 0) {
  if (dp[i][j] > dp[i - 1][j]) {
    solution.push(items[i].name);
    remain = remain - items[i].weight;
    j = remain;
    i--;
  } else {
    i--;
  }
}

console.log(solution);
