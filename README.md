# Simple distributed claims example

A simple distributed claims example using pyoidc.  These are lightly modified versions of the simple_op/simple_rp example that comes with pyoidc.

![Interacting services](imgs/diagram.png)

To run, add the following lines to `/etc/hosts`:

```
0.0.0.0 idp
0.0.0.0 rp
0.0.0.0 claims_provider
```

Run the services:

```
docker-compose up 
```

Then proceed to https://rp:8000 (note - self-signed certifcates, may cause some problems) and provide the IdP hostname (idp)

Then log in with:

user: diana pass: krall
* Faculty member
* Not project member

user: babs pass: howes
* Not faculty member
* Project member

user: upper pass: crust
* Faculty member
* Project member
