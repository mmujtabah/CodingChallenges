# Solution for Challenge IndexingMaster

theData = [[{"firstwall":{"secondwall":[{"thirdwall":[{"anythingelse":[],"fourthwall":{"fifthwall":[{"something":"else"},{"anything":"else"},{"somethingelse":"","hiddenwords":"dlrow olleh"}]}}]}]}}]]

theHiddenWord = theData[0][0]["firstwall"]["secondwall"][0]["thirdwall"][0]["fourthwall"]["fifthwall"][2]["hiddenwords"][::-1]
print(theHiddenWord)