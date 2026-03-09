import React from 'react';
import styles from './Nota.module.css';

export function Nota({ titulo = 'Nota', children }) {
    return (
        <div className={styles.nota}>
            <div className={styles.titulo}>💡 {titulo}</div>
            <div className={styles.contenido}>{children}</div>
        </div>
    );
}

export function Advertencia({ titulo = 'Advertencia', children }) {
    return (
        <div className={styles.advertencia}>
            <div className={styles.tituloAdvertencia}>⚠️ {titulo}</div>
            <div className={styles.contenido}>{children}</div>
        </div>
    );
}

export function Info({ titulo = 'Información', children }) {
    return (
        <details className={styles.info}>
            <summary className={styles.tituloInfo}>💡 {titulo}</summary>
            <div className={styles.contenido}>{children}</div>
        </details>
    );
}
