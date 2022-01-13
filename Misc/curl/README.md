# Sample curl commands

Basic sintax of a curl command:

```
curl [options] [URL...]
```

## GET

Simple straight-forward GET request. You don't even need to specify the request method since it defaults to GET, so piece-of-cake!

```
curl https://www.google.com
```

## POST

For POST, PUT, PATCH and so on (usually) you need to determine the request method, using `-X` or `--request`.
The option `-H` or `--header` adds extra headers. The option `-d` or `--data` adds a request body (a.k.a payload), which can point to a file as shown below, or be typed directly into the command, between quotes.

```
curl -X POST -H "Content-Type: application/json" \
 -H "Accept: application/json" \
 -d @payload.json \
 https://someniceapi.com/somecoolendpoint/v1
```

You can find more options, use cases, and explanations on the links below:

* https://www.computerhope.com/unix/curl.htm
* https://curl.se/docs/manual.html

More examples coming soon... :construction_worker:
