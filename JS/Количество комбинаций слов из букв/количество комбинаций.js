// Подсчет уникальных комбинаций слов в зависимости от количества разных символов.
// Например, буквы d, o, g. Варианты - dog, god, odg, ogd, dgo, gdo

function clunk(times) {
    let count = 0; // счетчик сколько раз вывелось слово clunk
    while (times > 0) {
        count += 1;
        console.log("clunk");
        console.log(" count = " + count);
        times = times - 1;
    }
    document.write("Количество комбинаций = " + count)
}


function get_size(size) {
    if (size == 0) {
        console.log("ноль комбинаций");
        alert("ноль комбинаций");
    } else if (size == 1) {
        console.log("одна комбинация");
        alert("одна комбинация");
    } else {
        let f = 1  // переменная - количество комбинаций, начиная с одной
        while (size > 1) {
            f = f * size;
            size = size - 1;
        }
        clunk(f);
    }
}


get_size(prompt("Введите количество символов: "))

// def clunk(times):
//     count = 0  # счетчик сколько раз вывелось слово clunk
//     while times > 0:
//         count += 1
//         print('clunk')
//         print(f' count = {count}')
//         times = times - 1


// def get_size(size):
//     if size == 0:
//         print("ноль комбинаций")
//     elif size == 1:
//         print("одна комбинация")
//     else:
//         f = 1  # переменная - количество комбинаций, начиная с одной
//         while size > 1:
//             f = f * size
//             size = size - 1
//         clunk(f)


// get_size(3)