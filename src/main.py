import sys
import os
import requests
import time
from Scene import Scene
from MLBSceneRenderer import MLBSceneRenderer
from GoogleNewsParser import GoogleNewsParser


def main():

    sceneRenderer = MLBSceneRenderer()
    parser = GoogleNewsParser()

    sceneRenderer.printText("Loading...")

    while True:
        try:
            parser.LoadPage()

            scene = Scene()
            scene.Home_Team_Logo_Image = parser.GetHomeTeamLogo()
            scene.Away_Team_Logo_Image = parser.GetAwayTeamLogo()
            scene.Home_Team_Score = parser.GetHomeTeamScore()
            scene.Away_Team_Score = parser.GetAwayTeamScore()
            scene.InningText = parser.GetInning()
            scene.AdditionalText = parser.GetAdditionalText()

            sceneRenderer.RenderScene(scene)
            time.sleep(30)
        except KeyboardInterrupt:
            quit()
        except TimeoutError:
            print("Request taking too long, starting over")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
