# jaclynfinnie.github.io-storage

This is a [jaclynfinnie.github.io](https://jaclynfinnie.github.io) database

## How to update data

`categories/[category]` 안에 `[name-of-path].md`를 작성하고 업데이트 한다.

이후 자동으로 post들의 정보가 담긴 `posts.json`이 업데이트 된다.

## Workflow when rebuilds & deployments

### Prerequisite

`main` branch의 변경 (commit & push)

### Github workflows

`categories/[category]/posts`를 읽어서 `posts.json`에 업데이트

`jaclynfinnie.github.io`에 update event dispatch
