fruits_basket1 = {"Apple","Banana","Pinapple"
                 "Grapps"}
fruits_basket2 = {"Kiwi","coconut","goava",
                  "mango"}

print("fruit_basket1:",fruits_basket1)
print("fruit_basket2:",fruits_basket2)


# PART 2: Add a new snack to snack_box1
fruits_basket1.add("tomato")
print("fruit_basket 1 after adding tomato:", fruits_basket1)

# PART 3: Find snacks common to both boxes
common_snacks = fruits_basket1.intersection(fruits_basket2)
print("Snacks in both baskets:", common_snacks)

# PART 4: Create an array of snack counts using the array module
import array as arr
fruit_counts = arr.array('i', [4, 6, 3, 5])
print("fruit counts array:", fruit_counts)

# PART 5: Add new snack counts to the array
fruit_counts.insert(0, 2)
fruit_counts.append(7)
print("fruit counts after adding items:", fruit_counts)

# PART 6: Count how many times the number 5 appears in the array
count_of_5 = fruit_counts.count(5)
print("Number of times 5 appears:", count_of_5)

# PART 7: Reverse the order of the snack counts array
fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)

# PART 8: Print the final school snack counter summary
print("")
print("===== SCHOOL SNACK COUNTER =====")
print("fruit_basket 1:", fruits_basket1)
print("fruit_basket 2:", fruits_basket2)
print("Shared fruit:", common_snacks)
print("fruit counts:", fruit_counts)
print("================================")

