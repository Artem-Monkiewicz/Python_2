/**
 * DOM przeglądarka interpretuje kod HTML i dostarcza obiekt, który JS jest w stanie odczytywać i modyfikować
 */

/**
 * obiekt document
 */

// document.body  // po kropce możemy dostać wiele pól związanych z naszym dokumentem
// najlepszą formą sprawdzenia co jest dostępne w obiekcie document jest sprawdzenie go w konsolo deweloperskiej w przeglądarce

/**
 * Tworzenie elementu
 *
 * 1) createElement
 *
 * 2) template string (backticki - znaki pojedynczego cudzysłowia po klawiszem esc) + właściwość innerHTML
 *
 */

const divElement = document.createElement("div");

const articleElement = document.createElement("article");

const funkcjaLicząca = () => 5000;

const result = funkcjaLicząca();

// articleElement.innerText = "Hello world!";
articleElement.innerHTML = `
    <h2>Hello world ${result}</h2>
    <input type="text" placeholder="Trelemorele"/>
`;

/* pobranie elmenetu main */
const mainElement = document.querySelector("main");

mainElement.appendChild(articleElement);

/**
 * Pobieranie elementów z dokumentu HTML
 */

// 1) metoda querySelector

// 2) metoda getElementById

// const firstDeleteButton = document.getElementById("firstDeleteButton");

// firstDeleteButton.classList.add("background-red");

// console.log(firstDeleteButton.classList.contains("deleteButton1"));

// // firstDeleteButton.remove();
// console.dir(firstDeleteButton);
// // firstDeleteButton.parentElement.parentElement.remove();

// firstDeleteButton.addEventListener("click", (event) => {
//   console.log(event);
//   event.target.parentElement.parentElement.remove();
// });

const usersStaticTable = document.getElementById("usersStaticTable");

usersStaticTable.addEventListener("click", (event) => {
  console.log(event.target);

  if (event.target.classList.contains("deleteButton")) {
    event.target.parentElement.parentElement.remove();
  }
});

/**
 * manipulowanie classami - lista klas jest dostępna pod polem classList
 * dodatkowo można manipulować tymi klasami przy pomocy dużej gamy metod dostępnej też pod tym polem
 */

// divElement.classList.add("super-div");

// divElement.classList.contains('super-div'); // sprawdzanie czy klasa instenieje zwraca true/false

// divElement.classList.replace("super-div", "super-span");

// divElement.classList.remove('super-div')

/**
 * Wstawianie elementu / osadzanie w dokumencie
 *
 * appendChild - metoda dostępna na każdym elemencie HTMLowym/Nodzie
 *
 * innerHTML - pole/właściwosć elementów HTMLowych/Nodów do której mozemy przypisać html napisanego za pomocą stringa
 *
 */

document.body.appendChild(divElement);

/**
 * Usuwanie elementu - metoda remove dostępna na elemencie HTML/Nodzie
 */

// document.body.remove()

/**
 * Eventy, event listnery - interakcja z UI
 */
