# Marvin

Marvin is a bot (and website!) written for the Judy2k Slack. It's a Django app, because that seemed the easiest way to chuck this thing together.

Marvin's main purpose is to welcome new members to the slack

- Introduce them to the code of conduct
- Encourage them to introduce themselves in #general (maybe ask them a bunch of questions and post the results in #general?)
- List useful channels they may be interested in.
- Encourage them to connect their Twitter account to the Slack's #social channel.

## To Do

- Log in with Slack
- Respond to `team_join` event with a welcoming DM
- Respond to `team_join` event with announcement in #general

- Request permission to join the Slack
- Authenticate with Twitter to allow tweets to be published to #social

## Open Ideas

- Can we do something with #secret-pint-club? Maybe a venue suggester, useful notifications, post details of the chosen venue?