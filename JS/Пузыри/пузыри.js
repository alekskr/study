let scores = [60, 50, 60, 58, 54, 54, 
    58, 50, 52, 54, 48, 69, 
    34, 55, 51, 52, 44, 51, 
    69, 64, 66, 55, 52, 61, 
    46, 31, 57, 52, 44, 18, 
    41, 53, 55, 61, 51, 44]

let costs = [0.25, 0.27, 0.25, 0.25, 0.25, 0.25, 
    0.33, 0.31, 0.25, 0.29, 0.27, 0.22, 
    0.31, 0.25, 0.25, 0.33, 0.21, 0.25, 
    0.25, 0.25, 0.28, 0.25, 0.24, 0.22, 
    0.20, 0.25, 0.30, 0.25, 0.24, 0.25, 
    0.25, 0.25, 0.27, 0.25, 0.26, 0.29]

document.write("Всего экземпляров: " + scores.length, "<br>");

// Вывод всех элементов массива
// let i = 0;
// while (i < scores.length) {
//     document.write("Элемент номер " + (i), " баллы: " + scores[i], "<br>");
//     console.log("Элемент номер " + (i), " баллы: " + scores[i], "<br>");
//     i += 1;
// }
// или:
// for (let i = 0; i < scores.length; i++) {
//     document.write("Элемент номер " + (i), " баллы: " + scores[i], "<br>");
//     console.log("Элемент номер " + (i), " баллы: " + scores[i], "<br>");
// }

// Вывод наибольшего элемента массива
function printAndGetHighScore(scores) {
let highScore = 0;
    for (let i = 0; i < scores.length; i++) {
        document.write("Элемент номер " + (i), " баллы: " + scores[i], "<br>");
        console.log("Элемент номер " + (i), " баллы: " + scores[i], "<br>");
        if (scores[i] > highScore) {
            highScore = scores[i];
            }
        }
    return highScore;
    }


// Индексы максимальных элементов
function getBestResults(scores) {
    let maxScoreIndex = [];
    for (let i = 0; i < scores.length; i++) {
        if (highScore == scores[i]) {
            maxScoreIndex.push(i);
        }
    }
    return maxScoreIndex;
}


// Минимальная стоимость
function minimumCosts(costs) {
    let minCost = 1;
    for (let i = 0; i < costs.length; i++) {
        if (minCost > costs[i]) {
            minCost = costs[i];
        }
    }
    return minCost;
}


// Лучший результат с минимальной стоимостью
function getMostCostEffectiveSolution(scores, costs, highScore) {
    let index;
    let cost = 1;
    for (let i = 0; i < scores.length; i++) {
        if (scores[i] == highScore) {
            if (costs[i] < cost) {
                cost = costs[i];
                index = i;
            }
        }
    }
    document.write("<br>Максимальный балл ", scores[index], " у образца # ", index, ", стоимость этого образца: ", cost);
    // return ("<br>Максимальный балл у образца #", index, " стоимость этого образца: ", cost);
}


highScore = printAndGetHighScore(scores);
console.log("Максимальный балл: ", highScore, "<br>");
document.write("Максимальный балл: ", highScore, "<br>");

bestResult = getBestResults(scores);
document.write("Элементы с наибольшим баллом: ", bestResult);
console.log("Элементы с наибольшим баллом: ", bestResult);

minCost = minimumCosts(costs);
document.write("<br>Минимальная стоимость: ", minCost);

getMostCostEffectiveSolution(scores, costs, highScore);