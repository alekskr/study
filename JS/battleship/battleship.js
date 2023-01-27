var location1 = Math.floor(Math.random(0, 4) * 5);  // функция Math.random генерирует случайное число от 0 до 1, 
                                                    // не включая 1. Функция Math.floor округляет число в сторону 
                                                    // уменьшения до ближайшего целого.
var location2 = location1 + 1;
var location3 = location1 + 2;
var guess
var guesses = 0
var hits = 0
var isSunk = false

while (isSunk == false) {
    guess = prompt("Готовсь! Цельс! Огонь! (введите число 0-6):");
    // функция promt используется для получения данных от пользователя
    // функция alert - для вывода окна с сообщением
    if (guess < 0 || guess > 6) {
        alert("Введите число 0-6!");
    } else if (guess == null) {
        break;
    } else {
        guesses += 1;
        if (guess == location1 || guess == location2 || guess == location3) {
            hits += 1;
            alert("Попадание!")
            if (hits == 3) {
                isSunk = true;
                alert("Корабль потоплен!")
                var stats = "<b>Корабль потоплен!<br>Точность стрельбы - " + (3/guess) + "</b>";
                // alert("Корабль потоплен! Точность стрельбы - " + (3/guess));
                document.write(stats);
            }
        } else {
            alert("Промах!")
        }
    }
}
document.write("<br>Количество попыток - ", guesses);
