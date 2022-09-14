#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

long long int LIM = pow(10, 3);
int expected = 9;

typedef struct ElitePrimes {
    long long int prime;
    long long int exponent;
    long long int value;
    struct ElitePrimes * next;
} ElitePrimes;

long long int * get_primes(long long int lim) {
    long long int *numbers = (long long int *) malloc(lim * sizeof(long long int)); // all integers from 0 to lim
    for (int i = 0; i < lim; i++) {
        *(numbers + i) = 1;
    }
    //memset((void *) numbers, (long long int) 1, lim); // set them all to 1
    *(numbers) = 0; // 0 is not a prime
    *(numbers+1) = 0; // 1 is not a prime
    long long int p = 2; // first prime
    // sieve of erathostenes
    while (p * p <= lim) {
        // set all multiples of the prime to 0
        long long int i;
        for (i = p+p; i <= lim; i += p){
            *(numbers + i) = 0;
        }
        // get next prime
        for (i = p+1; *(numbers + i) == 0; i++);
        p = i;
    }

    // now filter out all the numbers that are marked with 1 in char * numbers

    long long int count = 0;
    for (long long int i = 0; i < lim; i++) {
        if (*(numbers+i) == 1) {
            *(numbers+count) = i;
            count++;
        }
    }
    *(numbers+count+1) = 0;

    return numbers;
}

long long int helper(long long int expected) {
    switch(expected) {
        case 9:
            return 7;
        case 27:
            return 7 * 9;
        case 81:
            return 7 * 9 * 13;
        case 243:
            return 7 * 9 * 13 * 19;
        case 729:
            return 7 * 9 * 13 * 19 * 31;
        default:
            return 1;
    }
}

ElitePrimes * with_exponents(long long int * primes, long long int lim) {
    ElitePrimes *elite = (ElitePrimes *) malloc(sizeof(ElitePrimes)); // all integers from 0 to lim
    
    ElitePrimes *e_ptr = elite;

    for (long long int * ptr = primes; *ptr; ptr++) {
        long long int exponent = 1;
        long long int current = *ptr;
        while (current <= lim) {
            e_ptr->next = (ElitePrimes *) malloc(sizeof(ElitePrimes));
            e_ptr = e_ptr->next;
            e_ptr->prime = *ptr;
            e_ptr->exponent = exponent;
            e_ptr->value = current;
            e_ptr->next = NULL;

            current *= *ptr;
            exponent++;
        }
    }

    return elite->next;
}

// we call a prime p strong if and only if c(p) = 3
ElitePrimes * only_strong(ElitePrimes * elite, long long int lim) {
    ElitePrimes * last = (ElitePrimes *) malloc(sizeof(ElitePrimes *));
    ElitePrimes * first = last;
    ElitePrimes * ptr = elite;
    while (ptr != NULL){
        if (ptr->prime % 3 == 1 || (ptr->prime == 3 && ptr->exponent != 1)) {
            last->next = ptr;
            last = ptr;
            ptr = ptr->next;
            last->next = NULL;
        }
        else {
            ptr = ptr->next;
        }
    }

    return first->next;
}

int cmp_elite(const void * A, const void * B) {
    ElitePrimes ** a = (ElitePrimes **) (A);
    ElitePrimes ** b = (ElitePrimes **) (B);

    return (*a)->value - (*b)->value;
}

ElitePrimes * sort_elite(ElitePrimes *elite) {
    long long int length = 0;
    for (ElitePrimes * ptr = elite; ptr != NULL; ptr = ptr->next) {
        length++;
    }

    ElitePrimes * arr[length];

    long long int count = 0;
    for (ElitePrimes * ptr = elite; ptr != NULL; ptr = ptr->next) {
        *(arr+count) = ptr;
        count++;
    }
    
    qsort(arr, length, sizeof(ElitePrimes *), cmp_elite);

    // array to linked list of ElitePrimes
    ElitePrimes * start = (ElitePrimes *) malloc(sizeof(ElitePrimes));
    ElitePrimes * last = start;

    for (int i = 0; i < length; i++) {
        ElitePrimes * new = (ElitePrimes *) malloc(sizeof(ElitePrimes));
        new->prime = (*(arr+i))->prime;
        new->exponent = (*(arr+i))->exponent;
        new->value = (*(arr+i))->value;

        last->next = new;
        last = new;
    }
    last->next = NULL;
    return start->next;
}

long long int * get_primefactors(long long int n, long long int * primes) {
    long long int * factors = (long long int *) malloc(100 * sizeof(long long int)); // max 30 factors
    int count_factors = 0;
    long long int prime = *primes;
    int i = 0;
    while (prime * prime <= n) {
        if (n % prime == 0) {
            *(factors + count_factors) = prime;
            count_factors++;
            n = n / prime;
        }
        else {
            i++;
            prime = *(primes+i);
        }
    }

    if (n != 1) {
        *(factors + count_factors) = n;
        count_factors++;
    }
    *(factors + count_factors) = 0;
    return factors;
}

int c_is_one(long long int n, long long int * primes) {
    if (n < 7) {
        return 1;
    }
    if (n % 9 == 0) {
        return 0;
    }
    long long int * factors = get_primefactors(n, primes);
    for (long long int i = 0; *(factors+i) != 0; i++) {
        if (*(factors+i) % 3 == 1) {
            return 0;
        }
    }
    
    return 1;
}

long long int * calc_sum_of_no_effect(long long int limit, long long int * primes) {
    long long int * list = (long long int *) malloc((limit+1) * sizeof(long long int));
    long long int sum = 0;

    for (int i = 0; i < limit; i++) {
        if (c_is_one(i, primes)) {
            sum += i;
        }
        *(list+i) = sum;
    }

    return list;
}

long long int * calc_sum_of_no_effect_no_multiples_of_three(long long int limit, long long int * primes) {
    long long int * list = (long long int *) malloc((limit+1) * sizeof(long long int));
    long long int sum = 0;

    for (int i = 0; i < limit; i++) {
        if (i % 3 != 0 && c_is_one(i, primes)) {
            sum += i;
        }
        *(list+i) = sum;
    }

    return list;
}

void printer(ElitePrimes * list) {
    for (ElitePrimes * ptr = list; ptr != NULL; ptr = ptr->next) {
        printf("%I64d ^ %I64d = %I64d\n", ptr->prime, ptr->exponent, ptr->value);
    }
}

long long int multiplier(long long int n, long long int left, long long int * no_effect, long long int * no_effect_no_threes) {
    if (left == 1) {
        return 1;
    }
    else if (left == 2) {
        return 3;
    }

    if (n % 3 == 0) {
        return *(no_effect_no_threes+left);
    }
    else {
        return *(no_effect+left);
    }
}

long long int rec(long long int current, int i, int score, ElitePrimes * elite, long long int * no_effect, long long int * no_effect_no_threes) {
    if (score == expected) {
        return current * multiplier(current, LIM / current, no_effect, no_effect_no_threes);
    }

    long long int res = 0;
    for (ElitePrimes * ptr = (elite+i); ptr != NULL; ptr = ptr->next) {
        if (current % ptr->prime != 0) {
            long long int product = current * ptr->value;
            if (product > LIM) {
                break;
            }
            res += rec(current, i+1, score * 3, elite, no_effect, no_effect_no_threes);
        }
    }
    printf("%I64d: %I64d", current, res);
    return res;
}

int main() {
    time_t t = clock();

    long long int maximum = (LIM / helper(expected)) + 1;
    long long int * primes = get_primes(maximum);

    printf("Primes calculated: %f\n", (clock() - t) / 1000.0);

    time_t t1 = clock();
    ElitePrimes * elite = with_exponents(primes, maximum);
    printf("with exponents: %f\n", (clock() - t1) / 1000.0);

    time_t t2 = clock();
    elite = only_strong(elite, maximum);
    printf("only strong: %f\n", (clock() - t2) / 1000.0);

    time_t t3 = clock();
    elite =  sort_elite(elite);
    printf("sorted: %f\n", (clock() - t3) / 1000.0);

    time_t t4 = clock();
    long long int * no_effect = calc_sum_of_no_effect((LIM / helper(expected * 3)) + 1, primes);
    long long int * no_effect_no_threes = calc_sum_of_no_effect_no_multiples_of_three((LIM / helper(expected * 3)) + 1, primes);
    printf("sum of no effects: %f\n", (clock() - t4) / 1000.0);

    long long int res = rec(1, 0, 1, elite, no_effect, no_effect_no_threes);
    printf("Res: %I64d", res);


    printf("time taken %f\n", (clock() - t) / 1000.0);
    return 0;
}