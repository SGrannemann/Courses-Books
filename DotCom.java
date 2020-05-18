import java.util.ArrayList;

public class DotCom {
  private ArrayList<String> locationCells;
  int numOfHits = 0;
  private String name;

  public void setName (String nameOfDotCom) {
    name = nameOfDotCom;
  }
  public void setLocationCells (ArrayList<String> loc) {
    locationCells = loc;
  }

  public String checkYourself(String userInput) {
    String result = "miss";
    int index = locationCells.indexOf(userInput);
    if (index >= 0){
      locationCells.remove(index);
      if (locationCells.isEmpty()) {
        result = "kill";
        System.out.println("Ouch! You sunk " + name + " :(")
      } else {
        result = "hit";
      }
    }

      return result;
  } // close method
} // close class
