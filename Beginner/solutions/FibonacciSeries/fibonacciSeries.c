#include <stdio.h>

int main() {
    int num, first_term = 0, second_term = 1, next_term;

    // Get the number of terms from the user
    printf("Enter the number: ");
    scanf("%d", &num);

    // Print the first term (0)
    printf("%d ", first_term);

    // Loop to calculate and print the next terms of the Fibonacci series
    for(int i = 1; i < num; i++) {
        next_term = first_term + second_term; // Calculate the next term
        printf("%d ", next_term);            // Print the next term
        first_term = second_term;            // Update the first term
        second_term = next_term;             // Update the second term
    }

    return 0;
}
