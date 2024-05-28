import React from 'react';

function PlayerControls({isPlaying, setIsPlaying, skipSong}) {
    return (
        <div>
            <button onClick={() => skipSong(false)}>
                Назад
            </button>
            <button onClick={() => setIsPlaying(!isPlaying)}>
                {isPlaying ? 'Пауза' : 'Возобновить'}
            </button>
            <button onClick={() => skipSong()}>
                Вперёд
            </button>
        </div>
    );
}

export default PlayerControls;
