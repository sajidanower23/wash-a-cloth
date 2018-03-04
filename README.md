# Description

A script that is meant to be run as a cron job.

Based on the weather forecast obtained from the [Open Weather API](https://openweathermap.org/forecast5),
the script should send you an email letting you know if it's a bad idea to wash your clothes today.

# Getting started

Clone the repository, create a virtual environment and activate the virtualenv.
```console
cd
git clone git@github.com:sajidanower23/wash-a-cloth.git
cd wash-a-cloth
virtualenv env --python=`which python3`
```

Now, go to the [keys page](https://home.openweathermap.org/api_keys)
and get your API keys.

Open up `env/bin/activate` in an editor of your choice and add
these lines.

```bash
export APPID=... # your APPID
```

And finally,
`source env/bin/activate `

## TODO

 - [ ] Automate the process of making this a cron job
 - [ ] Make an approximated guess (based on the sunlight of that location) on how long it may take someone to dry their clothes

