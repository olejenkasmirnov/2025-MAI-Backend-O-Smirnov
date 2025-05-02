#Тест LRUCache

from LRU_Cache import LRUCache

def main():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    print(cache.get('Jesse'))  # 'James'
    cache.rem('Walter')
    print(cache.get('Walter'))  # ''

if __name__ == "__main__":
    main()