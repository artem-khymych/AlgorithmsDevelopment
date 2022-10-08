from datetime import datetime
FILEPATH_A = "C:/Users/user/Desktop/fileA.txt"
FILEPATH_B = "C:/Users/user/Desktop/file2.txt"
FILEPATH_C = "C:/Users/user/Desktop/file3.txt"


def writeSequence(flag, currentSequence,seriesB,seriesC):
   if flag:
      seriesB.extend(currentSequence)
   else:
      seriesC.extend(currentSequence)
   currentSequence.clear()


def readFile(FILEPATH):
   with open(FILEPATH) as file:
      data = file.read()
      data = data.strip()
   numbers = [int(num) for num in data.split(' ')]
   return numbers


def isSorted():
   numbers = readFile(FILEPATH_A)
   for i in range(len(numbers) - 1):
      if (numbers[i] > numbers[i + 1]):
         return False
   return True


def writeFile(series):
   seriesB=[]
   seriesC=[]
   for i in range(len(series)):
     if i %2 == 0:
        seriesC.append(" ".join(map(str, series[i])))
     else:
        seriesB.append(" ".join(map(str, series[i])))

   with open(FILEPATH_B,"w") as fileB:
      fileB.write(" ".join(map(str, seriesB)))
   with open(FILEPATH_C,"w") as fileC:
      fileC.write(" ".join(map(str, seriesC)))

def split():
   numbers=readFile(FILEPATH_A)
   currentSequence = []
   series = []
   currentSequence.append(numbers.pop(0))


   for number in numbers:
      if currentSequence[len(currentSequence) - 1] > number:
         series.append(currentSequence[:])
         currentSequence.clear()

      currentSequence.append(number)
   series.append(currentSequence[:])
   writeFile(series)


def readSeries(FILEPATH):
   numbers = readFile(FILEPATH)
   currentSequence = []
   series = []
   currentSequence.append(numbers.pop(0))

   for number in numbers:
      if currentSequence[len(currentSequence) - 1] > number:
         series.append(currentSequence[:])
         currentSequence.clear()

      currentSequence.append(number)
   series.append(currentSequence[:])
   return series


def merge():
   seriesB = readSeries(FILEPATH_B)
   seriesC = readSeries(FILEPATH_C)
   numbers = []
   serieNumber = 0
   while (serieNumber < len(seriesB) and serieNumber < len(seriesC)):

      i = j = 0
      while (i < len(seriesB[serieNumber]) and j < len(seriesC[serieNumber])):
         if seriesB[serieNumber][i] > seriesC[serieNumber][j]:
            numbers.append(seriesC[serieNumber][j])
            j += 1
         else:
            numbers.append(seriesB[serieNumber][i])
            i += 1
         if (i >= len(seriesB[serieNumber])):
            numbers.extend(seriesC[serieNumber][j:])
         elif j >= len(seriesC[serieNumber]):
            numbers.extend(seriesB[serieNumber][i:])
      serieNumber += 1


   if serieNumber > len(seriesB):
      for serieNumber in range(len(seriesC)):
         numbers.extend(seriesC[serieNumber][:])
         serieNumber += 1
   elif(serieNumber > len(seriesC)):
      for serieNumber in range(len(seriesB)):
         numbers.extend(seriesB[serieNumber][:])
         serieNumber += 1

   with open(FILEPATH_A, "w") as file:
      file.write(" ".join(map(str, numbers)))


start = datetime.now()
while not isSorted():
   split()
   merge()
print("sorting time ", datetime.now()-start)








