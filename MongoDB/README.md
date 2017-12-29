# MongoDB

## MongoDB Data Modeling

### Embedded Data Models

With MongoDB, you may embed related data in a single structure or document. These schema are generally known as “denormalized” models, and take advantage of MongoDB’s rich documents. As a result, applications may need to issue fewer queries and updates to complete common operations.

In general, use embedded data models when:

* You have “contains” relationships between entities.
* You have one-to-many relationships between entities. In these relationships the “many” or child documents always appear with or are viewed in the context of the “one” or parent documents.

However, embedding related data in documents may lead to situations where documents grow after creation. Document growth can impact write performance and lead to data fragmentation.

To interact with embedded documents, use *dot notation* to “reach into” embedded documents. e.g., consider the following collection:

```
db.inventory.insertMany( [
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);
```

The *dot notation* query to select all documents in whose size has uom = "cm" is:

```
db.inventory.find( { "size.uom": "cm" } )
```

### Normalized Data Models

Normalized data models describe relationships using references (Object Ids) between documents. In general, use normalized data models:

* When embedding would result in duplication of data but would not provide sufficient read performance advantages to outweigh the implications of the duplication.
* To represent more complex many-to-many relationships.
* To model large hierarchical data sets.

References provides more flexibility than embedding. However, client-side applications must issue follow-up queries to resolve the references. In other words, normalized data models can require more round trips to the server.

**Aditional Resources:**

- [Thinking in Documents (Part 1)](https://www.mongodb.com/blog/post/thinking-documents-part-1)
- [Thinking in Documents (Part 2)](https://www.mongodb.com/blog/post/thinking-documents-part-2)

## Atomicity

In MongoDB, operations are atomic at the document level. No **single** write operation can change more than one document. Operations that modify more than a single document in a collection still operate on one document at a time (operations that affect multiple embedded documents within that single record are still atomic). Ensure that your application stores all fields with atomic dependency requirements in the same document. If the application can tolerate non-atomic updates for two pieces of data, you can store these data in separate documents.

A data model that embeds related data in a single document facilitates these kinds of atomic operations. For data models that store references between related pieces of data, the application must issue separate read and write operations to retrieve and modify these related pieces of data.

## Indexes

Use indexes to improve performance for common queries. Build indexes on fields that appear often in queries and for all operations that return sorted results. MongoDB automatically creates a unique index on the _id field.

As you create indexes, consider the following behaviors of indexes:

* Each index requires at least 8 kB of data space.
* Adding an index has some negative performance impact for write operations. For collections with high write-to-read ratio, indexes are expensive since each insert must also update any indexes.
* Collections with high read-to-write ratio often benefit from additional indexes. Indexes do not affect un-indexed read operations.
* When active, each index consumes disk space and memory. This usage can be significant and should be tracked for capacity planning, especially for concerns over working set size.
