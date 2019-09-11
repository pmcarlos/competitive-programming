function HashTable(size) {
  this.buckets = Array(size)
  this.numBuckets = this.buckets.length
}

function HashNode(key, value, next) {
  this.key = key
  this.value = value
  this.next = next || null
}

HashTable.prototype.hash = function (key) {
  const total = key.split("").reduce((p, k) => p += k.charCodeAt(), 0)

  const bucket = total % this.numBuckets
  return bucket;
}

HashTable.prototype.insert = function (key, value) {
  const index = this.hash(key)
  const newHashNode = new HashNode(key, value)
  if (!this.buckets[index]) this.buckets[index] = newHashNode
  else if (this.buckets[index].key === key) {
    this.buckets[index].value = value
  } else {
    let currentNode = this.buckets[index]
    while (currentNode.next) {
      if (currentNode.next.key === key) {
        currentNode.next.value = value;
        return;
      }
      currentNode = currentNode.next
    }
    currentNode.next = newHashNode
  }
}

HashTable.prototype.get = function (key) {
  const index = this.hash(key)
  const bucket = this.buckets[index]
  if (!bucket) return null
  else {
    let currentNode = bucket
    while (currentNode) {
      if (currentNode.key === key) return currentNode.value
      currentNode = currentNode.next
    }
    return null
  }
}

HashTable.prototype.retrieveAll = function () {
  const allNodes = []
  for (let i = 0; i < this.numBuckets; i++) {
    let currentNode = this.buckets[i]
    while (currentNode) {
      allNodes.push(currentNode.key)
      currentNode = currentNode.next
    }
  }
  return allNodes
}

const myHT = new HashTable(30)

myHT.insert('Dean', 'dean@gmail.com');
myHT.insert('Megan', 'megan@gmail.com');
myHT.insert('Dane', 'dane@yahoo.com');
myHT.insert('Dean', 'deanmachine@gmail.com');
myHT.insert('Megan', 'megansmith@gmail.com');
myHT.insert('Dane', 'dane1010@outlook.com');