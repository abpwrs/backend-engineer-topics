# Backend Engineering Topics

## Context

Intern Alex was assigned the task of building a service with the following "requirements". 
He is struggling and could use some guidance and help with the implementation.

Requirements:
1. The service should allow a client to upload a set of files to S3
1. Once all files are uploaded, the service should emit an event using EventBridge
1. The emitted event must have a reference to all the files the client uploaded in that session
1. The service should be able to be run using docker
1. The service should support multiple clients simultaneously
1. The service should allow clients to upload multiple times / have multiple sessions

---

---

## Status

- [x] The service should allow a client to upload a set of files to S3
- [ ] Once all files are uploaded, the service should emit an event using EventBridge
- [ ] The emitted event must have a reference to all the files the client uploaded in that session
- [ ] The service should be able to be run using docker
- [ ] The service should support multiple clients simultaneously
- [ ] The service should allow clients to upload multiple times / have multiple sessions

## Problems

- Docker will build, but not run correctly. So I can only run this in my local env.
- I'm stuck on how to emit an event w/ a reference only to the files for the client's session.
- I'm not sure how / if I need to differentiate clients and sessions.
- How do I know when a client is done uploading?
- Docker takes a *long* time to build when I make even small changes to `main.py`.