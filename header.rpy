init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="MAS Otter's songs",
        description="New songs for Monika to sing.",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Otter's songs",
            user_name="my-otter-self",
            repository_name=otter_MAS_songs",
            submod_dir="/Submods/Otter's songs",
            extraction_depth=3,
            redirected_files=(
                "README.md",
            )
        )
