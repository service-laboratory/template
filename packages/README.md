# packages


### Build and publish backend
1. 
```
cd pypi/{package_name}
uv version --bump [patch|minor|major]
uv build .
uv publish --token {secret_token};
```

### Build and publish frontend
1. Create token in file .npmrc with format `//registry.npmjs.org/:_authToken={npmToken}`
2. Run command
```
cd npm/{package_name}
npm run build
npm publish --access public
```
