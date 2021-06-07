class Dog2 {
  String name;
  public static void main (String[] args) {
    // make a new dog variable and access it
    Dog2 dog1 = new Dog2();
    dog1.bark();
    dog1.name = "Bart";

    // now make a Dog array
    Dog2[] myDogs = new Dog2[3];
    // and put some dogs it
    myDogs[0] = new Dog2();
    myDogs[1] = new Dog2();
    myDogs[2] = dog1;

    // now access the Dogs using the array references
    myDogs[0].name = "Fred";
    myDogs[1].name = "Marge";

    // Hmmmm... what is myDogs[2] name?
    System.out.print("last dog's name is ");
    System.out.println(myDogs[2].name);

    // now loop through the array and tell all dogs to bark
    int x = 0;
    while (x < myDogs.length) {
      myDogs[x].bark();
      x = x + 1;
    }
  }
  public void bark() {
    System.out.println(name + " says Ruff!");
  }
}
