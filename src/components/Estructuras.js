import React from 'react';
import styles from './Ejercicio.module.css';

export function Ejercicio({ numero, titulo, children }) {
    return (
        <div className={styles.ejercicio}>
            <h3 className={styles.header}>
                <span className={styles.numero}>Ejercicio {numero}</span>
                {titulo && <span className={styles.titulo}>: {titulo}</span>}
            </h3>
            <div className={styles.body}>{children}</div>
        </div>
    );
}

export function Demostracion({ titulo, children }) {
    return (
        <div className={styles.demostracion}>
            <h3 className={styles.header}>
                <span className={styles.badge}>Demostración</span>
                {titulo && <span className={styles.titulo}>{titulo}</span>}
            </h3>
            <div className={styles.body}>{children}</div>
        </div>
    );
}

export function Enunciado({ titulo, children }) {
    return (
        <div className={styles.ejercicio}>
            <h3 className={styles.header}>
                <span className={styles.numero}>Enunciado</span>
                {titulo && <span className={styles.titulo}>: {titulo}</span>}
            </h3>
            <div className={styles.body}>{children}</div>
        </div>
    );
}
