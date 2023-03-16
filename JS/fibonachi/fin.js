let fib = [0, 1];


function func_fib(n) {
    for (let i = fib.length; i <= n; i++) {
        fib.push(fib[i - 1] + fib[i - 2]);
    }
    console.log(fib);
    console.log(fib[n]);
}

console.log("Fibonacci!");
func_fib(25);
