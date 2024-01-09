# MeisterTask Restorer

1. Get your MeisterTask API key from [here](https://www.mindmeister.com/api) in the section "Personal access tokens".
2. Find the right project for which you want to restore deleted tasks for by using `./getProject.py`.
3. Request all deleted tasks for that project by using `./getDeletedTasks.py`.
4. Restore all deleted tasks by using `./restoreDeletedTasks.py`.

**Replace all XXX with your own values.**

## Python basic commands

### Create virtual environment

```
python -m venv venv
```

### Activate virtual environment

```
.\venv\Scripts\activate
```

### Deactivate virtual environment

```
Deactivate
```
