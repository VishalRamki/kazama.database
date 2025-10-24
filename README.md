# kazama.database
The game database repo for the Kazama Game Save Data Sync application. This goal of this database is to store a collection of save locations for video games. This will prevent players from having to hunt their save data in increasingly convoluted locations across the many different locations.

These are the default save locations as defined by the developers/DRM Store. If you know or require custom locations to backup your save data you will have to add those manually on the [Kazama Game Save Sync Application](https://github.com/VishalRamki/kazama)'s `foldersyncs.toml` file.

## Using the database with Kazama Game Save Sync Application

At the moment the main application isn't setup to use the database. However, the next build of Kazama will feature it.

## Adding entries to the database

Feel free to add whatever game isn't there to the `database/entries/` folder using the following Template. Please open a PR request to push it into the `primary` branch.

template:

```json
{
  "id": 1778820, // this is the ID as it appears in its DRM (Steam, GOG)
  "platform": "windows", // this is the platform on which the game is played (WINDOWS, LINUX. MACOS)
  "drm": "Steam", // this is the game's Store DRM (STEAM, GOG, LINUXISOs)
  "name": "Tekken 8", // this is the name of the game including its version
  "folder": "C:\\Users\\{windows_user}\\AppData\\Local\\TEKKEN 8" // this is the default location of the save data, replace your windows/linux/mac username with {windows_user}, {linux_user}, or {mac_user}. The application will replace it when it loads.
}
```

## Closing

This is an open project for any and everyone to use and participate in. Feel free to use the data here as you see fit with or without the main Sync app.