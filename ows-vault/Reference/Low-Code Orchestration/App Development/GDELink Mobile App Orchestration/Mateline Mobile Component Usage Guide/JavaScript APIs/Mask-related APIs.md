---
title: "Mask-related APIs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731723210.html"
depth: 5
---
# Mask-related APIs

**NfLayout.showMask(message)**

Used to display the page mask. The page mask covers the entire page. As a result, all elements on the page cannot be clicked. This API is usually used to display the loading mask.

Input parameters:

**message** (string): Text displayed on the page mask

Example:

NfLayout.showMask(Nf.res("mask.processing"));

**NfLayout.loading(text,style,icon)**

Used to display the page loading mask. There is a dynamic loading circle.

Input parameters:

**text** (string): Displayed text

**style** (string): Loading circle color

 
| Value | Color Value |
| :-- | :-- |
| spinner-calm (default value) | #11c1f3 |
| spinner-stable | #f8f8f8 |
| spinner-positive | #387ef5 |
| spinner-light | #ffffff |
| spinner-balanced | #33cd5f |
| spinner-energized | #ffc900 |
| spinner-royal | #886aea |
| spinner-dark | #444444 | icon: String Pattern style of the loading circle

 
| Value | Style |
| :-- | :-- |
| spiral (default value) | Circular vortex, rotating at a constant speed |
| android | Default pattern of Android, rotating at an inconstant speed |
| ios | Default pattern of iOS, scattering from the center |
| ios-small | Mini version of the default iOS loading style |
| bubbles | Rotating bubbles |
| circles | Rotating circles |
| crescent | Rotating semicircles |
| dots | Horizontal dots (three dots) |
| lines | Vertical line waves, similar to the shape of a common audio |
| ripple | Ripples | Example:

// Default
NfLayout.loading();
// Customized
NfLayout.loading("Loading Service...","spinner-energized","lines");

**NfLayout.hideMask()**

Used to hide the page mask.

Input parameters: none

Example:

NfLayout.hideMask();

**Parent topic:** [[JavaScript APIs|JavaScript APIs]]