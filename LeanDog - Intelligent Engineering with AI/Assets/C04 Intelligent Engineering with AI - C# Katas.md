# Kata - Hello World

![LeanDog Logo](/Assets/LeanDog-logo.png)

## C# - Hello World

This project demonstrates the basic syntax and features of the C# programming language. The `Hello, World!` example is extended to include various types, conditionals, loops, collections, LINQ, exception handling, asynchronous programming, and syntax sugar features.

### Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) installed on your machine.

### Running the Project

This project is created using the dotnet CLI. Follow the steps below to build and run the C# file in your terminal:

```bash
~ cd HelloWorld
~ dotnet run
```

### Code Overview

Below is a detailed explanation of the features and syntax used in the `Program.cs` file:

#### Basic Output

The `Console.WriteLine` method is used to print text to the console.

```csharp
Console.WriteLine("Hello, World!");
```

#### Value Types

C# has several primitive value types, including `bool`, `byte`, `char`, `decimal`, `double`, `float`, `int`, and `long`.

```csharp
bool isActive = true;
byte byteValue = 255;
char charValue = 'A';
decimal decimalValue = 10.5m;
double doubleValue = 10.5;
float floatValue = 10.5f;
int intValue = 10;
long longValue = 100000L;
```

#### Reference Types

C# also supports reference types such as `object`, `string`, and `dynamic`.

```csharp
object obj = new object();
string str = "Hello";
dynamic dyn = "Dynamic typing";
```

#### Implicit vs Explicit Typing

You can declare variables using implicit (`var`) or explicit types.

```csharp
var i = 10; // Implicitly typed.
int x = 10; // Explicitly typed.
Console.WriteLine($"i={i}, x={x}");
```

#### Conditionals

Conditional statements in C# use `if`, `else if`, and `else`.

```csharp
var isTrue = false;
if (isTrue)
{
    Console.WriteLine("true");
}
else
{
    Console.WriteLine("false");
}
```

#### Collections: Arrays, Lists, and Dictionaries

C# supports various collection types, such as arrays, lists, and dictionaries.

```csharp
string[] weekDays = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
var optionList = new List<string> { "Option1", "Option2" };
var cities = new Dictionary<string, string>
{
    { "UK", "London, Manchester, Birmingham" },
    { "USA", "Chicago, New York, Washington" },
    { "India", "Mumbai, New Delhi, Pune" }
};
```

#### Loops

You can iterate over collections using loops like `foreach`.

```csharp
foreach (var kvp in cities)
{
    Console.WriteLine($"Key: {kvp.Key}, Value: {kvp.Value}");
}
```

#### Classes and Objects

Classes in C# are used to create objects with properties and methods.

```csharp
var helloWorld = new HelloWorld { Name = "Grogu" };
Console.WriteLine(helloWorld.Greeting());
```

---

# Kata - Fizz Buzz Kata

[Fizz Buzz: Coding Dojo](http://codingdojo.org/kata/FizzBuzz)

## Problem Description

Write a program that returns a list of numbers and strings from 1 to n, where n is the upper bound.

- For multiples of three, return “Fizz” instead of the number
- For multiples of five, return “Buzz”
- For numbers which are multiples of both three and five, return “FizzBuzz“
- Otherwise, return the ordinal number

**Upper bound**: 15  
**Example output**: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

## Run

Project created using dotnet CLI.

### In the terminal, build and run the project

```bash
dotnet test
```

## TDD Cycle

1. **Red**: Write a failing test case that defines a function or feature.
2. **Green**: Write just enough code to make the test pass.
3. **Refactor**: Clean up the code, ensuring that all tests still pass.

## Tips for Using GitHub Copilot in TDD

- **Generating Test Cases**: Start by writing the test cases. Use prompts to guide Copilot to generate these test cases.
  ```csharp
  // Prompt Copilot to create test cases
  [Fact]
  public void ShouldReturnFizzForMultiplesOf3()
  {
      // Copilot will suggest code here
  }
  ```
- **Implementing Minimal Code**: After your test case is written and fails, use Copilot to suggest minimal code to make the test pass.
  ```csharp
  public string FizzBuzz(int number)
  {
      // Copilot will suggest implementation
  }
  ```
- **Refactoring with Copilot**: Use Copilot to assist in refactoring the code to improve quality while keeping all tests green.

## Tips for Using GitHub Copilot Chat Plugin

- **Asking for Explanations**: If you are unsure about a particular piece of code, ask Copilot Chat to explain it.
  ```csharp
  // What does this method do?
  ```
- **Generating Code Snippets**: Request specific code snippets or solutions.
  ```csharp
  // Can you generate a method to check for multiples of 3 and 5?
  ```
- **Debugging Help**: Use the chat to get help on debugging issues.
  ```csharp
  // Why is my test failing?
  ```

## Potential Questions to Ask Tyler Morgan

- **Starting with TDD**: "How should I start TDD for the FizzBuzz problem?"
- **Writing Initial Tests**: "What are some good initial test cases for the FizzBuzz problem?"
- **Using AI Tools**: "How can I effectively use GitHub Copilot to assist with writing tests for FizzBuzz?"
- **Handling Edge Cases**: "What are some edge cases I should consider when writing tests for FizzBuzz?"
- **Refactoring Tips**: "How can I refactor my FizzBuzz code to ensure it's clean and maintainable?"