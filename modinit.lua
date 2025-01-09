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

    title = "Traduzione ITA (Beta 0.6)",
    description = "Traduzione dallo spagnolo mediante Gemini 1.5 Flash (LLM). La traduzione è parziale:\n- il non tradotto è in inglese\n- il tradotto è in test.\nStringhe tradotte: 66 %.",
    previewImagePath = "icon.png",
}