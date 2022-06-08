-- MountModData( "ITALIANO" )

local settings = 
{
    id = "italiano",
    name = "Italiano",

	font_settings = 
	{
	    title = { font = "fonts/titillium_sdf.zip", sdfthreshold = 0.36, sdfboldthreshold = 0.30 },
	    body = { font = "fonts/titillium_sdf.zip", sdfthreshold = 0.4, sdfboldthreshold = 0.33 },
	    button = { font = "fonts/titillium_sdf.zip", sdfthreshold = 0.4, sdfboldthreshold = 0.33 },
	    tooltip = { font = "fonts/titillium_sdf.zip", sdfthreshold = 0.4, sdfboldthreshold = 0.33 },
	    speech = { font = "fonts/titillium_sdf.zip", sdfthreshold = 0.4, sdfboldthreshold = 0.33 },
	},
    
    default_languages = 
    {
        "italiano",
    },
}

local function OnPreLoad( mod )
    Content.AddLocalization(settings)
    Content.AddPOFileToLocalization(settings.id, "ITALIANO:it.po")
end

    
return
{
    alias = "ITALIANO",
    OnPreLoad = OnPreLoad,

    title = "Italian Translation Mod (Alpha 0.3)",
    description = "The translation was made from the Spanish version through the use of an online translator. Therefore, any errors are the result of the translation approach used. With suggestions from the community, the mod will be updated, but it will take some time. I ask for your patience.",
    previewImagePath = "icon.png",
}