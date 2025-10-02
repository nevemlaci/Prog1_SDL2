#include <stdio.h>
#include <stdbool.h>
#include <SDL.h>

void on_quit(SDL_Window* window, SDL_Renderer* renderer) {
    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);
    SDL_Quit();
}

int main(int, char**) {
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        fprintf(stderr, "SDL failed to initialize! %s\n", SDL_GetError());
        return -1;
    }
    SDL_Window* window = NULL;
    SDL_Renderer* renderer = NULL;

    const int windowW = 800;
    const int windowH = 600;
    SDL_CreateWindowAndRenderer(windowW, windowH, 0, &window, &renderer);
    if (window == NULL) {
        fprintf(stderr, "Window failed to initialize! %s\n", SDL_GetError());
        return -1;
    }
    if (renderer == NULL) {
        fprintf(stderr, "Renderer failed to initialize! %s\n", SDL_GetError());
        return -1;
    }

    SDL_Event event;
    SDL_FRect rect = {.x = 30, .y = 50, .w = 100, .h = 100};
    while (true) {
        while (SDL_PollEvent(&event)) {
            switch (event.type) {
                case SDL_QUIT:
                    goto quit;
                default:
                    break;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 100, 200, 255);
        SDL_RenderClear(renderer);
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderFillRectF(renderer, &rect);
        SDL_RenderPresent(renderer);
    }

quit:
    on_quit(window, renderer);
    return 0;
}
