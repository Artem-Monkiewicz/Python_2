/**
 * ZMIENNE
 *
 * var
 *
 *
 * const
 * let
 *
 */
// ------------------------------------------------------------------------
// Wprowadzenie

// console.log(zmnienna)

// var zmnienna = 1213245;

// // console.log(name)

// zmnienna = "1234";

// const age = 123;

// let name = "John";

// // age = 123;

// console.log("String");
// console.log(name);
// console.log(age);

// ------------------------------------------------------------------------
// DALEJ
/**
 * console.log
 *
 * narzędzia deweloperskie
 */

/**
 * typy danych
 *
 * prymitywne:
 * string
 * number - (decimal, float, int) - to w jednym typie
 * boolean - TRUE / FALSE
 *
 * undefined - BRAK WARTOŚCI
 * null - NONE
 *
 * typy referencyjne
 * obiekty - słowniki
 * tablice
 * funkcje - składowe programu
 *
 */

// const stringStr = "Test2"; // rodzaj cudzysłowi nie ma znaczenia
// const przykładowyString = "HEj, {stringStr}";
// const przykładowyString1 = { stringStr };

// const stringBacktici = `werw
// er ${przykładowyString}    f
// ef ${przykładowyString}`;

// console.log(przykładowyString);
// console.log(przykładowyString1);
// console.log(stringBacktici);

// const olo1 = stringStr.includes("Te");
// console.log(olo1); // wyda true
// // stringStr.; // można i funkcji - dostępne w danym słowniku

// const olo2 = stringStr.length; // 5 odpowiedz
// console.log(olo2);

// const przykladowyNumber = 312.123; // wszystkie typy liczbowe są wrzucone do jednego
// const przykladowyBoolean = true; // false

// // wartości negatywne
// const przykładowyNull = null; // odpowiednik w pythonie
// let przykladowyUndefined = undefined;

// console.log(przykładowyNull);
// console.log(przykladowyUndefined);

// ------------------------------------------------------------------------
/**
 * funkcje warunkowe
 *
 *
 */

// if (stringStr === "Test2") {
//   console.log("Jupiii");
// }

// ------------------------------------------------------------------------

/**
 * Zadanie:
 * Napisz warunek który będzie sprawdzał
 * czy zmienna age jest większa niż 18 jeżeli tak wyświetl w konsoli informacje że user jest dorosły
 * w przeciwnym wypadku wyświetl wiadomosc odwrotną
 *
 * dodatkowo sprawdzaj czy wiek ma znaczenie dodając sprawdzenie w warunku zmiennej doesAgeMatter
 */

// console.log("Zadanie1");

// const age = 18;
// const doesAgeMatter = true;

// if (age >= 18 && doesAgeMatter) {
//   console.log("user jest dorosły");
// } else {
//   console.log("user nie jest dorosły");
// }

// ------------------------------------------------------------------------

/**
 * struktury danych
 * obiekty (słowniki) i tablice
 */

// obiekt
// const user = {
//   name: "John",
//   lastname: "Doe",
//   age: 16,
//   isAdult: false,
//   hobbies: ["Guitar", "Sport", "Dogs"],
// };

// //  Aktualizacja istniejących danych
// user.age = 20;
// user.isAdult = true;

// // dodawanie nowych kluczy/ pól do słownika/obiektu
// user.wzrost = 180;
// user.newKey = ["hey", 123];

// console.log(user);
// console.log(user.hobbies);

// // tablica
// // const todos = [123, "123", true, {}, null]
// const todos = ["Pouczyć się JSa", "Pouczyć się HTMLa"];

// // przypisanie nowej tablicy do zmiennej const nie jest możliwe

// //  dodawanie danych 1
// todos.push("Pouchyć się struktur danych");
// // dodawanie danych 2
// todos[3] = "Pouczyć się CSSa";

// console.table(todos);

// // edycja
// todos[0] = "JSa już umiem";
// console.table(todos);

// ------------------------------------------------------------------------

/**
 * Porównywanie obiektów za pomocą JSONa
 * !!!!!!!!!!!!parse!!!!!!!!!!!!!!!!!
 * 1) serializacja obiektów do JSONa
 * 2) porównać te 2 JSONy
 */

// ------------------------------------------------------------------------

/**
 * Obiekty są porównywane za pomocą referencji nie jest porównywana struktura
 */
// ------------------------------------------------------------------------
/**
 * Zdanie:
 * Utwórz obiekt (literał obiekt/słownik) user który będzie posiadał
 * następujące pola:
 *
 * name: string
 * lastName: string
 * age: number
 * todos: array of strings
 *
 *
 * Zadanie:
 * Utwórz listę/tablicę obiektów typu user niech lista będzie zawierała 3 elementy/obiekty
 *
 * rezultat możesz wykonsolować za pomocą console.table(users)
 */

// ------------------------------------------------------------------------

// console.log("Zadanie2");

// const user1 = {
//   name: "Artem",
//   lastname: "Monkiewicz",
//   age: 28,
//   isAdult: true,
//   hobbies: ["Uno", "Cats"],
//   todos: ["Nauczyć się Python", "Znależć nową pracę", "Skoczyć do toalety"],
// };

// console.log(user1);

// console.log("Zadanie3");

// const pora = ["Dzień", "Noc", "Wieczór"];
// console.table(pora);

// const tag = [
//   user,
//   user1,
//   {
//     name: "Gala",
//     lastname: "Such",
//     age: 24,
//     isAdult: true,
//     hobbies: ["Walk", "Rats"],
//     todos: [],
//   },
// ];
// console.log(tag);
// console.table(tag);

// ------------------------------------------------------------------------

/**
 * pętle
 *
 * for, while, do while
 *
 * funkcje wyższego rzędu
 *
 * map, filter, forEach
 */

// for (let i = 0; i < 10; i++) {
//   console.log("test");
// }

// for (let i = 0; i < tag.length; i++) {
//   console.log("test");
//   tag[i].isProcessed = true;
// }

// console.table(tag);

// //  Lambda
// tag.forEach((user, index) => {
//   if (user.age >= 18) {
//     console.log(`${user.name} is adult`);
//   }
// });
// ------------------------------------------------------------------------

/**
 * Zadanie
 * Przeiteruj się przez tablicę userów
 * i sprawdż czy userzy są dorośli (age > 18) jeżeli tak ustaw nowo dodane pole isAdult na true
 * w przeciwnym wypadku ustaw je na false
 */

// const user11 = {
//   name: "Bill",
//   lastName: "Cosby",
//   age: 13,
// };

// const user22 = {
//   name: "Bill",
//   lastName: "Cosby",
//   age: 23,
// };

// const user33 = {
//   name: "John",
//   lastName: "Rambo",
//   age: 70,
// };

// const user44 = {
//   name: "Janet",
//   lastName: "Jackson",
//   age: 15,
// };

// console.log("Zadanie3");

// 1

// const users5 = [user11, user22, user33, user44];
// users5.forEach((user) => {
//   if (user.age >= 18) {
//     user.isAdult = true;
//   } else {
//     user.isAdult = false;
//   }
// });

//2

// const users5 = [user11, user22, user33, user44];

// users5.forEach((user) => {
//   user.isAdult = user.age > 18;
// });

// console.table(users5);

// ------------------------------------------------------------------------

/**
 * funkcje
 *
 * function
 *
 * arrow functions
 */

// function exampleVoidFunction() {
//   console.log("Hej, jestem pustą funkcją, nic nie zwracam ");
// }

// function addTwoNumbers(number1, number2) {
//   const sum = number1 + number2;
//   return sum;
// }

// const sumam = addTwoNumbers(2, 4);
// console.log(sumam);

// 1:

// const subTwoNumbers = () => {}

// 2:
// const subTwoNumbers = () =>

// const subTwoNumbers = (n1, n2) => {
//   return n1 - n2;
// };

// const subTwoNumbers2 = (n1, n2) => n1 / n2;

// function exampleVoidFunction() {
//     console.log("Hej jestem funkją pustą bo nic nie zwracam");
//   }

//   function addTwoNumbers1(number1, number2) {
//     const sum = number1 + number2;
//     /**
//      * ciało funkcji
//      */
//     return sum;
//   }

//   const addTwoNumbers2 = (number1, number2) => {
//     const sum = number1 + number2;
//     /**
//      * ciało funkcji
//      */
//     return sum;
//   };

//   const addTwoNumbers3 = (number1, number2) => number1 + number2;

//   const sum123 = addTwoNumbers1(123, 321);

//   console.log(sum123);

//   const subTwoNumbers = (n1, n2) => {
//     return n1 - n2;
//   };

//   const divideTwoNumbers = (n1, n2) => n1 / n2;

//   const addAgesOfTwoUsers = (user1, user2) => {
//     return user1.age + user2.age;
//   };

//   const result = addAgesOfTwoUsers(
//     { name: "John", age: 20 },
//     { name: "Jerry", age: 30 }
//   );
//   console.log(result);

//   // function isUserAdult(user){
//   //   if(user.age > 18){
//   //     return true
//   //   }else {
//   //     return false
//   //   }
//   // }

//   // function isUserAdult(user){
//   //  return user.age > 18;
//   // }

//   function isUserAdult(user) {
//     if (typeof user === "object" && !!user && user.age) {
//       return user.age > 18;
//     }

//     return "Nie poprawne dane";
//   }

//   const result1 = isUserAdult(null);
//   const result2 = isUserAdult("");
//   const result3 = isUserAdult();
//   const result4 = isUserAdult(123);
//   const result5 = isUserAdult({ age: 20 });
//   const result6 = isUserAdult({ age: 16 });

//   console.table([result1, result2, result3, result4, result5, result6]);

//   /**
//    * Zadanie:
//    * stwórz funkcje isUserAdult zwracająca true lub false w zależności czy user przekazany w parametrze ma age>18
//    *
//    * ** obsłuż przypadek gdy do funkcji przekazane są nie poprawne dane
//    *
//    * Zadanie:
//    * stwórz funkcje getAvarageAge która przyjmie tablicę użytkowników i zwróci średnią arytmetyczną wieku użytkówników
//    *
//    *
//    * ** Zadanie
//    * stwórz funckje getNumbersOfAdultsPerGender która przyjmie tablicę/listę użytkowników i zwróci obiekt
//    * z dwoma kluczami numberOfAdultMales i numberOfAdultFemales
//    *
//    * {
//    *    numberOfAdultMales: 25,
//    *    numberOfAdultFemales: 12
//    * }
//    *
//    *
//    */

//   const getAvarageAge = (users) => {
//     let sum = 0;
//     users.forEach((user) => {
//       // sum = user.age + sum;
//       sum += user.age;
//     });

//     return sum / users.length;
//   };

//   const avgAge = getAvarageAge(users5);

//   console.log(avgAge);

//   function getNumbersOfAdultsPerGender() {
//     /**
//      * Miejsce na Twój kod
//      */
//     return {
//       numberOfAdultMales: undefined,
//       numberOfAdultFemales: undefined,
//     };
//   }
