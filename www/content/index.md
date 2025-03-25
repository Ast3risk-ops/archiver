---
title: Home
navigation: false
toc: false
---
::hero
---
announcement:
  title: 'Now on top.gg!'
  icon: 'simple-icons:topdotgg'
  to: 'https://top.gg/bot/1311438512045949029'
  target: '_blank'
actions:
  - name: Documentation
    rightIcon: lucide:arrow-right
    leftIcon: lucide:book-open-text
    to: /setup
  - name: Install the app
    rightIcon: lucide:arrow-up-right
    leftIcon: simple-icons:discord
    variant: outline
    to: https://discord.com/oauth2/authorize?client_id=1311438512045949029
    target: _blank
---

#title
Archive Discord messages just like emails

#description
Never lose another message again.
::

<div class="rounded-xl" align="center">
<video src="/assets/vid/hero.mp4" height="1840" width="968" controls autoplay loop muted playsinline></video>
</div>

<p class="scroll-m-20 text-2xl font-semibold tracking-tight [&:not(:first-child)]:mt-8" align="center">With Archiver, you can conveniently keep a record of whatever messages you want.</p>

::card-group
  ::card
  ---
  title: Simple
  icon: lucide:arrow-right-to-line
  to: /setup/quickstart#start-archiving
  showLinkIcon: false
  horizontal: true
  ---
  #description
  Just right click and save any message.
  ::
  ::card
  ---
  title: Free
  icon: lucide:badge-dollar-sign
  to: https://discord.com/oauth2/authorize?client_id=1311438512045949029
  target: _blank
  rel: noopener noreferrer
  showLinkIcon: false
  horizontal: true
  ---
  #description
  No paywalls or limits. Ever.
  ::
  ::card
  ---
  title: Informative
  icon: lucide:badge-info
  to: /usage/features
  showLinkIcon: false
  horizontal: true
  ---
  #description
  View information about any archived message, even if it's been deleted.
  ::
  ::card
  ---
  title: Private
  icon: lucide:eye-off
  to: /terms/privacy-policy
  showLinkIcon: false
  horizontal: true
  ---
  #description
  Your archive belongs to you and you alone.
  ::
::

:h2[FAQ]
:br
::collapsible
#title
How do I use the app?

#content
See our [quickstart guide](/setup/quickstart) or run `/help`.
::

<br>

::collapsible
#title
Where can I see updates?

#content
They're posted on the [changelog page](/changelog) (major releases) and [Github commits](https://github.com/Ast3risk-ops/archiver/commits/main/){ target="_blank" rel="noopener noreferrer" } (small changes).
::

<br>

::collapsible
#title
Why not use Forwards?

#content
Discord's built-in forwarding feature does allow you to store messages somewhere, but you won't get much information on them (only link and timestamp, not even author information). You also lose what little information is given if the message or server is deleted (since the link won't work). Forwards from DMs will have no link or timestamp. You also can't forward polls.
::

<br>

::collapsible
#title
Can I use this app in a guild?

#content
Yes! Just click **Add to Server**. It will be available to all your members if installed. We're hoping to add extra features for guild install in the future.
::

<br>

::collapsible
#title
I'm having a problem, where do I report it?

#content
Make a [Github issue](https://github.com/Ast3risk-ops/archiver/issues/new/choose){ target="_blank" rel="noopener noreferrer" } or go to our [support server](https://discord.gg/d3a9dW9KHN){ target="_blank" rel="noopener"}.

::

:h2[Team]

::team-card-group
  ::team-card
  ---
  avatar: https://github.com/Ast3risk-ops.png
  name: Asterisk
  title: Lead Developer
  links:
    - icon: lucide:earth
      to: https://asterisk.lol
    - icon: ri:mastodon-line
      to: https://social.linux.pizza/@asterisk
    - icon: lucide:github
      to: https://github.com/Ast3risk-ops
    - icon: radix-icons:discord-logo
      to: https://discord.com/users/789561823863111742
  ---
  ::
::
