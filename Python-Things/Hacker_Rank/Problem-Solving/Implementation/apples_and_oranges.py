def apples_and_oranges():
   samHouseCoordinates = list(map(int, input().split()))
   appleAndOrangeTreesCoordinates = list(map(int, input().split()))
   appleAndOrangeCount = list(map(int, input().split()))
   applesDistance = list(map(int, input().split()))
   orangesDistance = list(map(int, input().split()))

   print(len([x + appleAndOrangeTreesCoordinates[0] for x in applesDistance
              if x + appleAndOrangeTreesCoordinates[0] >= samHouseCoordinates[0] and x + appleAndOrangeTreesCoordinates[0] <= samHouseCoordinates[1]]))
   print(len([y + appleAndOrangeTreesCoordinates[1] for y in orangesDistance if y + appleAndOrangeTreesCoordinates[1]
              >= samHouseCoordinates[0] and y + appleAndOrangeTreesCoordinates[1] <= samHouseCoordinates[1]]))

apples_and_oranges()
