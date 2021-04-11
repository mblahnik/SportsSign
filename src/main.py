import sys
import os
import requests
import time
from Scene import Scene
from MLBSceneRenderer import MLBSceneRenderer
from MLBSceneGenerator import MLBSceneGenerator


def main():

    sceneGenerator = MLBSceneGenerator()
    sceneRenderer = MLBSceneRenderer()
    parser = GoogleNewsParser()

    sceneRenderer.printText("Loading...")

    while True:
        try:
            scene = sceneGenerator.GetScene()
            sceneRenderer.RenderScene(scene)
            time.sleep(30)
        except KeyboardInterrupt:
            quit()
        except:
            print("Trying again...")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
