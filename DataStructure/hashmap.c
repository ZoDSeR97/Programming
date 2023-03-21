#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 2
#define LOAD_FACTOR 0.75

typedef struct Node
{
    char *key;
    int value;
    struct Node *next;
} Node;

typedef struct
{
    Node **buckets;
    int capacity;
    int size;
    int threshold;
} HashMap;

void free_node(Node *node)
{
    if (node == NULL)
        return;
    free(node->key);
    free(node);
}

void free_map(HashMap *map)
{
    for (int i = 0; i < map->capacity; i++)
        free_node(map->buckets[i]);

    free(map->buckets);
    free(map);
}

unsigned long hash(const char *key)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *key++) != '\0')
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}

void resize(HashMap *map, int new_capacity)
{
    map->buckets = realloc(map->buckets, new_capacity * sizeof(Node *));
    if (map->buckets == NULL)
    {
        // handle allocation failure
        fprintf(stderr, "OUT OF MEMORY: Failed to reallocate memory for bucket array\n");
        exit(EXIT_FAILURE);
    }

    // Initialize new buckets to NULL
    for (int i = map->capacity; i < new_capacity; i++)
        map->buckets[i] = NULL;

    // Redistribute elements for new hash
    for (int i = 0; i < map->capacity; i++)
    {
        Node *node = map->buckets[i];
        while (node != NULL)
        {
            Node *next = node->next;
            int index = hash(node->key) % new_capacity;
            node->next = map->buckets[index];
            map->buckets[index] = node;
            node = next;
        }
        map->buckets[i] = NULL;
    }
    map->capacity = new_capacity;
    map->threshold = (int)(new_capacity * LOAD_FACTOR);
}

void put(HashMap *map, const char *key, int value)
{
    if (map->size >= map->threshold)
        resize(map, map->capacity*2);

    int index = hash(key) % map->capacity;
    Node *node = map->buckets[index];
    while (node != NULL)
    {
        if (strcmp(node->key, key) == 0)
        {
            node->value = value;
            return;
        }
        node = node->next;
    }
    Node *new_node = malloc(sizeof(Node));
    if (new_node == NULL)
    {
        // handle allocation failure
        fprintf(stderr, "OUT OF MEMORY: Failed to allocate memory for new node\n");
        exit(EXIT_FAILURE);
    }
    new_node->key = strdup(key);
    if (new_node->key == NULL)
    {
        // handle allocation failure
        fprintf(stderr, "OUT OF MEMORY: Failed to allocate memory for new key\n");
        exit(EXIT_FAILURE);
    }
    new_node->value = value;
    new_node->next = map->buckets[index];
    map->buckets[index] = new_node;
    map->size++;
}

int get(HashMap *map, const char *key)
{
    int index = hash(key) % map->capacity;
    Node *node = map->buckets[index];
    while (node != NULL)
    {
        if (strcmp(node->key, key) == 0)
            return node->value;
        node = node->next;
    }
    return -1;
}

int main()
{
    HashMap *map = malloc(sizeof(HashMap));
    map->buckets = calloc(INITIAL_CAPACITY, sizeof(Node *));
    map->capacity = INITIAL_CAPACITY;
    map->size = 0;
    map->threshold = (int)(INITIAL_CAPACITY * LOAD_FACTOR);

    put(map, "apple", 1);
    put(map, "banana", 2);
    put(map, "orange", 3);

    printf("%d\n", get(map, "apple"));
    printf("%d\n", get(map, "banana"));
    printf("%d\n", get(map, "orange"));
    
    free_map(map);

    return 0;
}