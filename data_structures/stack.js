class Stack {
  constructor() {
    this.storage = []
    this.count = 0
  }

  // push an element to the stack
  push = (element) => {
    this.storage[this.count] = element
    console.log(`${element} is pushed on ${this.count}`)
    this.count += 1
    this.print()
    return;
  }

  print = () => {
    console.log(this.storage)
    return;
  }

  // pop an element from the stack
  pop = () => {
    if (this.count === 0) {
      return undefined
    }
    this.count -= 1
    delete this.storage[this.count]
    this.storage = this.storage.filter(el => el != undefined)
    this.print()
    return
  }

  // return the number of items inside the stack
  size = () => {
    console.log(`Size of the stack is ${this.count}`)
    return this.count
  }
}

const myStack = new Stack()

myStack.push(100)
myStack.push(200)
myStack.push(300)
myStack.push(400)
myStack.push(500)
myStack.pop()
myStack.pop()
myStack.pop()
