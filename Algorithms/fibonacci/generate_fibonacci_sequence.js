// https://leetcode.com/problems/generate-fibonacci-sequence/
/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    // multiple yields are the breakpoints in a javascript debugger within a single function. Until you tell to navigate next breakpoint it wont execute the code block. (Note: without blocking the whole application)
    yield 0;
    yield 1;
    let arr = [0,1]
    while (true) {
        arr.push(arr[arr.length-1] + arr[arr.length-2])
        yield arr[arr.length-1]
    }

};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */