// Define a class called "Person"
class Person {
  // Constructor to initialize the properties
  constructor(public name: string, public age: number) {}

  // Method to display information about the person
  displayInfo() {
    console.log(`Name: ${this.name}, Age: ${this.age} years old`);
  }
}

// // Create an instance of the Person class
// const person1 = new Person("Alice", 30);
//
// // Call the displayInfo method to display the information
// person1.displayInfo();

