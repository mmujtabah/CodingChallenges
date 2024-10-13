const theData = [{ firstwall: { secondwall: [{ thirdwall: [{ anythingelse: [], fourthwall: { fifthwall: [{ something: "else" }, { anything: "else" }, { somethingelse: "", hiddenwords: "dlrow olleh" }] } }] }] } }]


var encryptedHiddenWord = theData[0]["firstwall"]["secondwall"][0]["thirdwall"][0]["fourthwall"]["fifthwall"][2]["hiddenwords"]

function reverseString(string) {
    string.split('').reverse().join('')
}

var theHiddenWord = reverseString(encryptedHiddenWord)

console.log(theHiddenWord) // hello world