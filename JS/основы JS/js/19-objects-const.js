// ================================ 10. Нюанс сonst и изменением объекта и массива ===============================

const person = {
	userName: 'Марк',
	age: 30,
	isMarried: false,
};

// Ошибка! Переопределение ссылки на новый объект
person = {
	userName: 'Ник',
};

// Аналогично и для массивов
